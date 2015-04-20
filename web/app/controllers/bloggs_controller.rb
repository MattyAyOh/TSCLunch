class BloggsController < ApplicationController
  http_basic_authenticate_with name: "dhh", password: "secret", except: [:index, :show]

  def index
    @articles = Blogg.all
  end

  def show
    @article = Blogg.find(params[:id])
  end

  def new
    @article = Blogg.new
  end

  def edit
    puts 'EDITING'
    puts params
    @article = Blogg.find(params[:id])
  end

  def create
    @article = Blogg.new(article_params)

    if @article.save
      redirect_to @article
    else
      render :new
    end
  end

  def update
    @article = Blogg.find(params[:id])
    puts 'LOOK AT ME!!!'
    puts article_params
    if @article.update(article_params)
      redirect_to @article
    else
      render :edit
    end
  end

  def destroy
    @tempBlog = Blogg.find(params[:id])
    @tempBlog.destroy

    redirect_to bloggs_path
  end

  private
  def article_params
    params.require(:blogg).permit(:title, :text)
  end
end
